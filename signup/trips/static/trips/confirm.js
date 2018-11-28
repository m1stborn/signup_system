  　var t=3;//設定跳轉的時間
　　setInterval("refer()",1000); //啟動1秒定時
　　function refer(){
　　　　if(t==0){
　　　　　　location.href="/"; //#設定跳轉的鏈接地址
　　　　}
　　　　document.getElementById('show').innerHTML=""+t+"秒後自動跳轉"; // 顯示倒計時
　　　　t--; // 計數器遞減
　　　　//本文轉自：
　　}