import time
import threading
from typing import Dict
from database import get_pending_extractions, update_extraction_status, get_extraction
from main import extract_complete_github_api
import os

class ExtractionWorker:
    def __init__(self, check_interval: int = 5):
        self.check_interval = check_interval
        self.running = False
        self.worker_thread = None
        self.current_processing = set()
    
    def start(self):
        if self.running:
            return
        
        self.running = True
        self.worker_thread = threading.Thread(target=self._worker_loop, daemon=True)
        self.worker_thread.start()
        print("Extraction worker started")
    
    def stop(self):
        self.running = False
        if self.worker_thread:
            self.worker_thread.join(timeout=10)
        print("Extraction worker stopped")
    
    def _worker_loop(self):
        while self.running:
            try:
                pending = get_pending_extractions(limit=5)
                
                for extraction in pending:
                    extraction_id = extraction['id']
                    
                    if extraction_id in self.current_processing:
                        continue
                    
                    self.current_processing.add(extraction_id)
                    thread = threading.Thread(
                        target=self._process_extraction,
                        args=(extraction,),
                        daemon=True
                    )
                    thread.start()
                
                time.sleep(self.check_interval)
            
            except Exception as e:
                print(f"Error in worker loop: {e}")
                time.sleep(self.check_interval)
    
    def _process_extraction(self, extraction: Dict):
        extraction_id = extraction['id']
        
        try:
            print(f"Processing extraction {extraction_id}")
            update_extraction_status(extraction_id, 'processing')
            
            start_url = extraction['start_url']
            tool_name = extraction['tool_name']
            api_base_url = extraction['api_base_url']
            
            if not api_base_url:
                raise ValueError("API base URL is required")
            
            result = extract_complete_github_api(
                start_url=start_url,
                tool_name=tool_name,
                api_base_url=api_base_url
            )
            
            if isinstance(result, tuple):
                result_path, endpoint_count = result
            else:
                result_path = result
                endpoint_count = None
            
            output_path = str(result_path)
            
            update_extraction_status(
                extraction_id=extraction_id,
                status='completed',
                output_path=output_path,
                endpoint_count=endpoint_count
            )
            
            print(f"Extraction {extraction_id} completed successfully: {output_path}")
        
        except Exception as e:
            error_message = str(e)
            print(f"Error processing extraction {extraction_id}: {error_message}")
            update_extraction_status(
                extraction_id=extraction_id,
                status='failed',
                error_message=error_message
            )
        
        finally:
            self.current_processing.discard(extraction_id)

worker = ExtractionWorker()

