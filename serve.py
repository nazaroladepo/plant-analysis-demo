#!/usr/bin/env python3
"""
Simple HTTP server for Vue.js SPA with history mode routing.
This server serves index.html for all routes to support client-side routing.
"""

import http.server
import socketserver
import os
from urllib.parse import urlparse

class SPAHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        # If it's a file that exists, serve it normally
        if os.path.isfile(path.lstrip('/')):
            super().do_GET()
        else:
            # For all other routes, serve index.html (SPA routing)
            self.path = '/index.html'
            super().do_GET()

if __name__ == "__main__":
    PORT = 8000
    
    with socketserver.TCPServer(("", PORT), SPAHandler) as httpd:
        print(f"🌱 Plant Analysis Demo Server")
        print(f"📡 Serving at http://localhost:{PORT}")
        print(f"🔧 SPA Mode: All routes serve index.html")
        print(f"⏹️  Press Ctrl+C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n👋 Server stopped")