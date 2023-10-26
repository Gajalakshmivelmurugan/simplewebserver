from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
         <title>revenue generating software companies</title>
         <body>
                <table border="6" cellspacing="4" cellpadding="4">
                    <caption>Top five revenue generating software companies</caption>
                    <tr>
                         <th>s.no</th>
                         <th>company</th>
                         <th>revenue</th>
                    </tr>

                    <tr>
                         <th>1</th>
                         <th>microsoft</th>
                         <th>65 billion</th>
                    </tr>

                    <tr>
                         <th>2</th>
                         <th>oracle</th>
                         <td>29.6 billion</td>
                    </tr>

                    <tr>
                         <th>3</th>
                         <th>IBM</th>
                         <th>29.1 billion</th>
                    </tr>

                    <tr>
                         <th>4</th>
                         <th>SAP</th>
                         <th>6.4 billion</th>
                    </tr>

                    <tr>
                         <th>5</th>
                         <th>symantec</th>
                         <th>5.6 billion</th>
                    </tr>

                </table>
      </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()