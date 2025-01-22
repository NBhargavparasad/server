import http.server
import socketserver
import argparse

# Define the handler to serve files from the current directory
Handler = http.server.SimpleHTTPRequestHandler

def start_server(port):
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print(f"Serving HTTP on port {port} (http://localhost:{port}/)\nUse Ctrl+C to stop the server.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")
            httpd.server_close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start a simple HTTP server.")
    parser.add_argument(
        "-p", "--port", type=int, default=8000, help="Specify the port number (default: 8000)"
    )
    args = parser.parse_args()

    start_server(args.port)
