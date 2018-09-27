# signup_system
123test
宗佑要看學姊熱褲



Local 端

確認目前所在的 branch：git branch

切換到 master：git checkout master

更新 master：git pull origin master

開新的 branch：git branch <branch-name>（名字不要亂取，依任務命名）

切換到到該 branch，git checkout <branch-name>，在此 branch 上開發開發過程中，定期 commit
完成一階段任務，例如：完成修改 sidebar、修改某些檔案

git add <檔案>，確認即將要 commit 的檔案

git commit -m <commit message>（commit message 寫清楚）
  
完成任務後，git push origin <branch-name>（不要直接 push 到 origin master，很危險）
GitHub

開 pull request

pull request 中寫明此 branch 做了什麼
打上 fix #<issue 編號>
請別人來看，沒問題後再 merge，merge 之後該 branch 會自動被刪掉

常見問題
Q: 切換到別的 branch 時，如果該 branch 有未 commit 的檔案會切不過去，該怎麼辦？
A: 可以 git stash 先暫存改過但尚未 commit 的檔案，切回來之後再 git stash pop。可是除非你很清楚你在做什麼，否則不建議這麼做！
Q. 改了一堆檔案，git add <檔案> 時超麻煩耶
A: 不太建議 git add -A 一次加入所有檔案，因為有時候會 commit 不該 commit 的檔案，所以還是慢慢加吧～



#data too long  
SET @@global.sql_mode= 'NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';  
  
grant all privileges on signup_system .* to mist@localhost identified by "password";

- msyql.server start  
- mysql -u root -p  
- use signup_system;//指定資料庫  
- DESC trips_visitor;  
- SELECT * FROM trips_visitor;  
/lambda
