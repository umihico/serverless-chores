import socket
import slack

host="umihi.co"
ideal={80: 'open', 443: 'open', 22: 'close', 3306: 'close'}
ports=list(ideal.keys())

def is_open(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    return sock.connect_ex((host,port))

def portscan():
    results={}
    for port in ports:
        result_int=is_open(port)
        results[port]="open" if result_int==0 else 'close'
        if results[port]!=ideal[port]:
            slack.error('port', port, 'is', results[port].upper()+"!!", socket.errno.errorcode[result_int]+" "+result_int if result_int!=0 else "")
    slack.log(results)
    return results

def test_portscan():
    results=portscan()
    for port, result in ideal.items():
        assert port in results and results[port]==result
    print(results)

if __name__ == '__main__':
    test_portscan()
