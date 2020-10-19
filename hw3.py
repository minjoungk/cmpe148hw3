from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server

mailServer = 'localhost'
mailPort = 25

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((mailServer, mailPort))
recv = clientSocket.recv(1024)
print 'test'
print recv
if recv[:3] != '220':
    print '220 reply not received from server.'

# Send HELLO command and print server response.
helloCommand = 'HELO Alice\r\n';
clientSocket.send(helloCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
    print '250 reply not received from server.'

# Send MAIL FROM command and print server response.

mail_from = 'MAIL FROM: <mail@mail.com>\r\n.'
clientSocket.send(mail_from)
recv1 = clientSocket.recv(1024)
print(recv1)
if recv1[:3] != '250':
    print('mail from 250 reply not received from server.')

# Send RCPT TO command and print server response.
rctp_to = 'RCPT TO: <myemail@mail.com>\r\n'
clientSocket.send(rctp_to)
recv2 = clientSocket.recv(1024)
print(recv2)
if recv1[:3] != '250':
    print('rcpt to 250 reply not received from server.')

# Send DATA command and print server response
data = 'Data'
print(data)
clientSocket.send(data)
recv3 = clientSocket.recv(1024)
print(recv3)
if recv1[:3] != '250':
    print('data 250 reply not received from server.')

# Send message data.
message = raw_input('Enter Message Here: ')

# Fill in end# Message ends with a single period.
singlePeriod = '\r\n.\r\n'
clientSocket.send(message + singlePeriod)
recv4 = clientSocket.recv(1024)
print(recv4)
if recv1[:3] != '250':
    print('end msg 250 reply not received from server.')

# Send QUIT command and get server res.
quit = 'Quit\r\n'
print(quit)
clientSocket.send(quit)
recv5 = clientSocket.recv(1024)
print(recv5)
if recv1[:3] != '250':
    print('quit 250 reply not received from server.')

