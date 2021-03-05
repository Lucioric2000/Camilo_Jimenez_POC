dispcover = "Y"
disprss = "Y"
dispethdashboard = "Y"
dispbtcdashboard = "Y"
dispportfolio = "Y"
dispinvest = "Y"

fiat={{user.fiat}}

coverspecialcoin1 ="cardano"

# your defipulse API key. https://data-beta.defipulse.com/dashboard/egs
#defipulseApikey = "3c078480f89a7fa220f2b91a7244ea17b5bab77e3cff6b0fa1e2d0ed22c"
#defipulseApikey = "e61b012ae1c05cd4f84bd87c86826ec28f2fde511db9e73fddf9a0a510d0" #defipulse
#defipulseApikey = "eb186b54317ca712f06413fbff21359c742e22ee11c181c692791e1d103a" #ethgasstation
#defipulseApikey = "06f9063a11d3f6d69594c9304d074cde1f92f4dfe86b1668704da3a12cee"
#defipulseApikey = "93c078480f89a7fa220f2b91a7244ea17b5bab77e3cff6b0fa1e2d0ed22c"
defipulseApikey = "74719cfc77511f9f1a709bc60d5f1c3d6383518a631e2a820bfbc88b7f00"
#defipulseApikey = "7e586257575cab0b247acf0d2fddef28c0a9c537808cba24257a03c1ca3c"

glassnodeapikey="c1fc75c3-ab0d-4025-9512-6952f97423b4"
coinmarketcapkey="8aea8bc7-4ae6-4728-81e4-d3a03c5dc6d1"

colorscheme="green"

myportfolio = 	['0x9ec5e68f807b56befed7d99e9fcec6111845e7b7',
				'0x8998aC6F6d538207015F11E0aCfE7300FBa350E1',
				'0x82eaa009e9cae43955a3ef9d1de3bf68f5154200',
				'0xb5eEcF93B18E3F03F0593B21f9fCb4E2f9b56cf3',
				'0x15FF39F7BdA0eB22a38f56e379e3ded6A14f842D',  #this is the drive-me-crazy address
				'0x03F2C52f1Cd2043AF5AD4B9C16B689B2B28bD8Ac',
				'0x8998aC6F6d538207015F11E0aCfE7300FBa350E1']
				
interval = 120000  # waiting time between slides  300,000 = around 5 minutes 120000 = 2 mins per slide (exact number is 500sec for all 4 slides)

# Your 2 coins/tokens. Needs to match coingeckos names. For example: https://api.coingecko.com/api/v3/coins/uniswap
ETHspecialcoin1 = "ripple"
ETHspecialcoin2 = "cardano"

override="N"

#display tresholds (change color if x value increased more than y%). 
dispprice1hrchangediff = "Y"  # recommended pricechangediff=2
dispprice24hrchangediff = "N" # recommended pricechangediff=5
pricechangediff = 2

# URL that offer RSS feeds; alternative (checked Oct 2020): http://coinnews247.com/rss-feeds-per-category/ or https://blog.feedspot.com/cryptocurrency_rss_feeds/ 
rssurl = 'https://news.bitcoin.com/feed/'
#rssurl = 'https://www.newsbtc.com/feed'   not working with feedparser
#rssurl = 'https://cryptocontrol.io/feed'
#rssurl = 'https://www.coindesk.com/feed'
#rssurl = 'https://cointelegraph.com/rss/tag/ethereum'
##rssurl = 'https://www.cryptoninjas.net/feed/'


#display tresholds (change color if x value increased more than y%). 
#price1hrchangediff = 1
#price24hrchangediff = 5
disppricebtc1hrchangediff = 2
dispmarketcap24h = 2
disphashrate24hrdiff =1
dispmempooldiff = 25
dispaverage_transaction_fee_usd_24hdiff = 10