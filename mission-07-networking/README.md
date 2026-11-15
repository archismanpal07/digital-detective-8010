# Mission 7 - How computers communicate

## 1. Task / objective
Explain common network concepts, perform a DNS lookup and connectivity check, and describe the steps involved in opening a website.

## 2. Work completed

### Task 7.1: Network concepts

| Concept | Explanation | Example |
|---|---|---|
| LAN | Connects devices across a small area. | Home or school Wi-Fi network |
| MAN | Connects networks across a city or large campus. | City-wide public network |
| WAN | Connects devices or networks over large geographic areas. | The Internet |
| DNS | Looks up the network address associated with a domain name. | Resolving `example.com` |
| Router | Forwards data between networks. | Home router connecting a local network to an internet provider |
| Protocol | Agreed rules for communication. | HTTPS for secure web traffic |
| Packet switching | Sends information in packets across network links. | A web page response sent over the Internet |
| Client-server | A client requests a service and a server responds. | Browser requesting a page from a web server |

### Task 7.2: Network observations
- A connectivity test checks whether a destination responds over the network. `ping -c 1 -W 3000 example.com` received one reply with 0% packet loss during this check.
- `dig example.com +noall +answer` returned DNS A records `172.66.147.243` and `104.20.23.154` at the time checked. DNS answers can change.
- When a domain is entered in a browser, DNS helps find an address for the server. The browser can then send the request to that address.
- These are public example-domain answers; no local IP address, Wi-Fi name, or account detail is recorded.

### Task 7.3: What happens when a website opens?
1. The user enters a domain name in a browser.
2. The browser asks DNS to resolve the name to an IP address.
3. DNS returns an address for the website's server.
4. The client computer sends the request through the local network and router.
5. The server receives the request and sends back a response.
6. The browser interprets the response data and displays the page to the user.

## 3. Commands / tools used
- `dig example.com +noall +answer` - looked up DNS A records for the example domain.
- `ping -c 1 -W 3000 example.com` - sent one connectivity test packet and received a reply.
- Git - committed and pushed this mission checkpoint.

## 4. My understanding
A domain name is easier to remember than a numeric network address. DNS provides an address lookup, and a router forwards network traffic toward its destination. Client-server communication lets a browser request information and a server send a response, usually using agreed protocols.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- `mission-07-networking/README.md` - network concepts, command observations, and website request steps.

## 8. Commit details
- **Commit message:** `Explain networking concepts and website communication`
- **Status:** To be pushed and verified on GitHub.
