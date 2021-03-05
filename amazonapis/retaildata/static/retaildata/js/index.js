function download(filename, text) {
	var element = document.createElement('a');
	console.log (text);
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', filename);
    element.style.display = 'none';
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
} 

function generate_variables_py(coin_name){
	var interval = document.getElementById("interval").value * 60000

	var dispprice1hrchangediff = "N"
	if($(document.getElementById("price1hrchangediff")).is(":checked")){
		dispprice1hrchangediff="Y";
		dispprice24hrchangediff="N";
		}else{
		dispprice1hrchangediff="N";
		dispprice24hrchangediff="Y";
		}

	var dispcover = "N"
	if($(document.getElementById("cover")).is(":checked")){
		dispcover="Y";
		}else{
		dispcover="N";
		}
	var disprss = "N"
	if($(document.getElementById("rss")).is(":checked")){
		disprss="Y";
		}else{
		disprss="N";
		}
	var dispportfolio = "N"
	if($(document.getElementById("portfolio")).is(":checked")){
		dispportfolio="Y";
		}else{
		dispportfolio="N";
		}
	var dispethdashboard = "N"
	if($(document.getElementById("ethdashboard")).is(":checked")){
		dispethdashboard="Y";
		}else{
		dispethdashboard="N";
		}
	var dispbtcdashboard = "N"
	if($(document.getElementById("btcdashboard")).is(":checked")){
		dispbtcdashboard="Y";
		}else{
		dispbtcdashboard="N";
		}
	var dispinvest = "N"
	if($(document.getElementById("investment")).is(":checked")){
		dispinvest="Y";
		}else{
		dispinvest="N";
		}
	// Generate download of hello.txt file with some content
	var text = 
	"dispcover = " + '"' + dispcover + '"\n' +
	"disprss = " + '"' + disprss + '"\n' +
	"dispethdashboard = " + '"' + dispethdashboard + '"\n' +
	"dispbtcdashboard = " + '"' + dispbtcdashboard + '"\n' +
	"dispinvest = " + '"' + dispinvest + '"\n' +
	"dispportfolio = " + '"' + dispportfolio + '"\n' +
	"fiat = " + '"' + document.getElementById("fiat").value + '"\n' +
	"override =" + '"N"\n' +
	"coverspecialcoin1 = " + '"' + coin_name + '"\n' +
	"defipulseApikey = " + '"' + document.getElementById("defipulseApikey").value + '"\n' +
	"colorscheme=" + '"' + document.getElementById("colorscheme").value + '"\n' +
	"myportfolio =" + '[\'' + document.getElementById("myportfolio").value + '\']\n' +
	"interval = " + interval + '\n' +
	"ETHspecialcoin1 = " + '"' + document.getElementById("ETHspecialcoin1").value + '"\n' +
	"ETHspecialcoin2 = " + '"' + document.getElementById("ETHspecialcoin2").value + '"\n' +
	"dispprice1hrchangediff = " + dispprice1hrchangediff + '\n' +
	"dispprice24hrchangediff = " + dispprice24hrchangediff + '\n' +
	"pricechangediff = " + document.getElementById("pricechangediff").value + '\n' +
	"rssurl = " + '"' + document.getElementById("rssurl").value + '"\n' +
	"disppricebtc1hrchangediff = " + document.getElementById("disppricebtc1hrchangediff").value + '\n' +
	"dispmarketcap24h = " + document.getElementById("dispmarketcap24h").value + '\n' +
	"disphashrate24hrdiff =" + document.getElementById("disphashrate24hrdiff").value + '\n' +
	"dispmempooldiff = " + document.getElementById("dispmempooldiff").value + '\n' +
	"dispaverage_transaction_fee_usd_24hdiff = " + document.getElementById("dispaverage_transaction_fee_usd_24hdiff").value;
	var filename = "variables.py";
	download(filename, text);

}
// Start file download.
document.getElementById("dwn-btn").addEventListener("click", function(){
	//var coin_name = $("#coverspecialcoin1").val();
	var coin_name = document.getElementById("coverspecialcoin1").value;
    $.ajax({
        url: 'https://api.coingecko.com/api/v3/coins/'+coin_name,
        dataType: 'json',
        success: function (data) {
            //alert("The coin name " + coin_name + " is correct");
            generate_variables_py(coin_name);
        },
        error: function(xhr, status) {
            alert("The coin " + coin_name + " does not exist");
        }
    });
}, false);
