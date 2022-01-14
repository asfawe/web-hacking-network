from time import time
import asyncio
import aiohttp 

#Subdomain Dictionary File
#https://bit.ly/3j9es5e
wordlist_path="./subdomains.txt"
target_domain="google.com"


async def asnyc_func(domains):
    conn=aiohttp.TCPConnector(limit_per_host=10)
    async with aiohttp.ClientSession(connector=conn) as s:
        futures=[
            asyncio.create_task(discover_url(s, f"http://{domain}.{target_domain}"))
            for domain in domains
        ]
        results=await asyncio.gather(*futures)
        
async def discover_url(s, domain):
    try:
        async with s.get(domain) as r:
            if r.status==200:
                output=(domain, r.status)
                print(output)
                return output
            else:
                raise Exception("status_code", r.status)
    except aiohttp.client_exceptions.ClientConnectionError as e:
        pass
    except Exception as e:
        status_code, error_status=e.args
        output=(domain, error_status)
        print(output)
        return output
    
    
if __name__=="__main__":
    begin=time()
    subdomain_words=open(wordlist_path).read().splitlines()
    asyncio.run(asnyc_func(subdomain_words))
    end=time()
    print(f"실행 시간: {end-begin}")