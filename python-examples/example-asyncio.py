import asyncio
import time

def main():
    async def read_and_write_file(file_path):
        with open(file_path) as f,open('hh.py') as w:
            content = f.read()
            w.write(content)
    
    asyncio.get_event_loop()
    
            