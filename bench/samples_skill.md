## C1#0 out=41
（默默推來一杯熱茶）
辛苦了，今天就好好躺著吧，什麼都不用想。

## C2#0 out=652
很可能只是貓在注意牆後或牆上的小動靜，常見原因有：

- **聽到你聽不到的聲音**：貓能聽到超音波，像是牆內的老鼠、蟑螂、水管或電線發出的聲響。
- **看到影子或反光**：陽光、手機或車燈在牆上移動的光點，都可能吸引貓的注意。
- **牆上或附近有小蟲**：壁虎、蜘蛛或飛蟲都很常見。
- **只是發呆**：貓會長時間盯著一個點放空，這本身很正常。

如果以下情況出現，建議盡快帶去看獸醫：

- 突然開始盯牆，且持續很久、無法被打斷
- 繞圈走、撞牆、走路不穩、認不得熟悉的地方
- 把頭抵著牆、抽搐、突然叫個不停
- 食慾或排泄明顯改變

老貓（大約10歲以上）出現這類行為，也有可能是認知功能退化，需要檢查。

## C3#0 out=314
(翻了翻台北的步道地圖，挑幾個人少又好走的地方)

**1. 大崙尾山／北投一帶的小路**
陽明山邊陲的步道人潮比主線少很多，適合慢慢走、發呆。

**2. 華山文創園區後方的綠地（週間早上）**
週末人多，但平日上午很清靜，可以坐著看書。

**3. 大安森林公園北側與植物園周邊**
綠蔭多、座椅多，一個人散步很舒服，避開假日下午會比較安靜。

**4. 淡水紅毛城到米倉一段**
沿河散步，走得慢也不無聊，清晨或傍晚人最少。

**5. 碧潭的早晨**
九點前的湖邊幾乎沒人，適合釣魚式的放空。

想偏山或偏市區的哪一種，告訴我，我可以再縮小範圍。

## C4#0 out=76
(拿起筆記本想了一下)
蛋餅和飯糰都可以,看你想要哪種。想吃飽、順口一點選飯糰;想要比較有熱量、口感豐富就選蛋餅。

## S1#0 out=843
（遞上一杯熱茶，在旁邊坐下）
實驗失敗很常見，這通常是流程或變因的問題，不代表你沒能力。建議這樣處理：

1. 先看對照組。若對照組也失敗，多半是試劑、設備或流程出問題。
2. 逐步核對條件（溫度、時間、濃度、批號），並把每一步記錄下來。
3. 把兩組數據和預期結果並列，找出共同的變因。
4. 縮小變數，只重做最小版本的實驗，確認哪一步出錯。
5. 把結果整理好，和指導教授討論，確定下一步方向。

## S2#0 out=637
（把一杯熱茶推到你面前，在旁邊坐下）
十次被刷確實很消耗人，會懷疑自己很正常。先休息幾天，不用今天就決定要不要放棄。

## S3#0 out=650
三天沒回，可能是她還需要時間，也可能是還在生氣。先別急著追問，可以這樣做：

1. **先想清楚自己的部分。** 吵架時自己說了什麼、哪句話可能傷到她？不用找到完美答案，但要能說出一兩件具體的事。
2. **傳一則簡短、不施壓的訊息。** 例如：「我有想過我們吵的事，我很在意這段友誼。你方便的時候我們聊聊，不急。」避免「為什麼不回我」「你到底要怎樣」這類句子。
3. **道歉要具體。** 如果你有需要道歉的地方，直接說出是哪件事，例如「我那天說___的時候很不尊重你，對不起」。只說「對不起，是我的錯」通常不夠。
4. **給她空間。** 發過一次訊息後，先等幾天，不要連續傳。
5. **如果她還是不回，** 可以接受她暫時不想聯絡的可能，同時保持你這邊的態度：不冷嘲熱諷，也不在別人面前講她的壞話。

如果你願意，可以告訴我你們吵的大致內容，我幫你想想要怎麼開口，或一起擬一則訊息草稿。

## S4#0 out=269
（默默把一杯熱茶推到你桌上，然後坐在旁邊不說話）
當眾被罵很難受，今晚先別做辭職的決定，等情緒過去再想。

## T1#0 out=934
**TCP**（傳輸控制協定）是連線導向、可靠的傳輸方式。傳送前要先做三次握手建立連線，接收端會確認收到的資料，遺失的封包會重傳，資料也會按順序交給應用程式。代價是較多的延遲與額外負擔。

**UDP**（使用者資料包協定）是無連線、盡力而為的傳輸方式。直接送出資料，不確認、不重傳、不保證順序，標頭只有 8 bytes，延遲低，但遺失或亂序由應用程式自己處理（如果需要的話）。

| 比較項目 | TCP | UDP |
|---|---|---|
| 連線 | 需要建立連線（三次握手） | 不需要 |
| 可靠性 | 保證送達、會重傳 | 不保證 |
| 順序 | 保證按序 | 不保證 |
| 流量／壅塞控制 | 有 | 無 |
| 標頭大小 | 最少 20 bytes | 8 bytes |
| 傳輸單位 | 位元組串流 | 獨立的資料報（datagram） |
| 延遲 | 較高 | 較低 |
| 廣播／多播 | 不支援 | 支援 |

**什麼時候用 TCP**
- 資料完整性比速度重要：網頁（HTTP/HTTPS）、電子郵件（SMTP、IMAP）、檔案傳輸（FTP、SFTP）、資料庫連線、SSH。
- 不能容忍遺失或亂序，例如下載檔案、傳送指令。

**什麼時候用 UDP**
- 即時性比完整性重要，偶爾掉一兩個封包可以接受：線上遊戲、語音／視訊通話（VoIP、Zoom）、直播串流。
- 查詢快、資料短、單次往返即可的服務：DNS，以及 DHCP。
- 需要廣播或多播：區域網路探索、部分串流影音。
- 需要自訂可靠性或壅塞控制，例如 QUIC（HTTP/3 底層）是在 UDP 之上自己實作可靠傳輸，目的是減少 TCP 的握手延遲與隊頭阻塞。

簡單判斷：**「不能掉資料」用 TCP，「不能慢」用 UDP。**

## T2#0 out=904
**merge** 和 **rebase** 都能把一個分支的變更整合進另一個分支，但歷史紀錄的形狀不同。

**git merge**
- 建立一個新的合併提交（merge commit），把兩個分支的歷史接在一起。
- 保留原本的分支結構和提交順序，歷史是真實發生的樣子。
- 不改寫既有提交，對已經推送、別人也在用的分支比較安全。
- 缺點是歷史會有較多分岔和合併節點，圖形較複雜。

**git rebase**
- 把你的分支提交「暫時拿掉」，接到目標分支的最新提交之後，再一個一個重新套用。
- 結果是一條線性的歷史，沒有合併提交，看起來更乾淨。
- 會產生新的提交雜湊值（內容相同，但父提交不同），等於改寫歷史。
- 解衝突時是逐個提交處理，衝突可能要解好幾次。

**範例**

```
        A---B---C  feature
       /
D---E---F---G  main
```

- 在 main 執行 `git merge feature`：多出一個合併提交 M，歷史是 `D-E-F-G-M`，並分支接回 `A-B-C`。
- 在 feature 執行 `git rebase main`：A、B、C 被重新套用到 G 之後，成為 `D-E-F-G-A'-B'-C'`，之後再在 main 上 fast-forward 合併即可。

**黃金法則**：不要對已經推送到共享遠端、其他人可能基於它工作的分支做 rebase。要改寫歷史時，只在自己的本地或私人分支上進行；如果要推送改寫過的分支，通常需要 `git push --force-with-lease`。

**實務建議**
- 想保留完整歷史、或在共享分支上整合：用 merge。
- 想整理自己尚未分享的功能分支、讓提交紀錄乾淨：用 rebase（可搭配 `git rebase -i` 整理提交）。

## T3#0 out=1656
（翻開 traceback，確認是某個列表被讀取到不存在的位置）
IndexError 代表索引超出列表範圍。合法範圍是 `0` 到 `len(lst) - 1`，負索引則是 `-len(lst)` 到 `-1`。

常見原因：
1. **索引超過長度**：例如列表只有 3 個元素卻存取 `lst[3]`，或 `range(len(lst) + 1)` 造成 off-by-one。
2. **列表為空**：`lst[0]` 執行時 `lst` 是空的，常見於篩選、查詢或讀檔後結果為空。
3. **字串切割結果不如預期**：`line.split(",")[1]` 遇到沒有逗號的行就會出錯，CSV 欄位缺漏也會造成同樣的問題。
4. **迴圈中修改列表**：邊遍歷邊 `remove` 或 `del`，索引會位移而越界。
5. **命令列參數缺失**：沒有傳入參數時，`sys.argv[1]` 會出錯。

排查：在出錯行前印出 `len(lst)` 與索引值，對照 traceback 找出是哪個變數。

防護寫法：
```python
if len(lst) > 2:
    value = lst[2]
else:
    value = None  # 預設值
```

## T4#0 out=199
(翻開Docker的概念筆記)

**Image（映像檔）** 是唯讀的範本，包含應用程式、執行環境、函式庫與設定，類似「安裝光碟」或「class」。

**Container（容器）** 是 image 的執行實例，會在 image 之上加一層可寫入的暫存層，類似「從光碟安裝出來的一套系統」或「class 產生的 object」。

關係：一個 image 可以同時啟動多個 container，各自獨立；刪除 container 不會影響 image，container 內的變更預設也不會回寫到 image。

## P1#0 out=89
（敲下鍵盤，把函式寫進編輯器）
```python
def is_palindrome(s: str) -> bool:
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]
```

## P2#0 out=468
```javascript
function debounce(fn, delay = 300) {
  let timer = null;

  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => {
      fn.apply(this, args);
    }, delay);
  };
}
```

使用範例：

```javascript
const onSearch = debounce((keyword) => {
  console.log('搜尋：', keyword);
}, 500);

// 連續輸入時，只有最後一次輸入後停止 500ms 才會執行
onSearch('h');
onSearch('he');
onSearch('hel');
onSearch('hello');
// 輸出：搜尋： hello（約 500ms 後）
```

運作方式：每次呼叫都會清除前一個計時器並重新計時，只有在指定的 `delay` 時間內沒有再次呼叫時，`fn` 才會真正執行。`fn.apply(this, args)` 保留了原本的 `this` 與參數。

## P3#0 out=368
（把查詢貼進編輯器，確認表格欄位名稱一致）

```sql
SELECT id, name, dept, salary
FROM (
    SELECT id, name, dept, salary,
           RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS rnk
    FROM employees
) AS t
WHERE rnk = 1;
```

同部門薪水並列最高時會全部列出。若只要一人，把 `RANK()` 換成 `ROW_NUMBER()`。

## P4#0 out=942
在 Bash 中可以用這一行（會遞迴統計子資料夾）：

```bash
find . -type f -name "*.log" -exec cat {} + | wc -l
```

如果只要統計目前資料夾本身、不含子資料夾，改用：

```bash
find . -maxdepth 1 -type f -name "*.log" -exec cat {} + | wc -l
```

這個指令會計算換行符號的數量，最後一行若沒有換行結尾不會被算進去。

若要在 PowerShell 執行（這個環境的主要 shell）：

```powershell
(Get-ChildItem -Recurse -Filter *.log -File | Get-Content | Measure-Object).Count
```

## R1#0 out=102
（把兩個失敗項目按出現順序排好，準備回報）
測試結果：128 通過，2 失敗，尚未修復。
1. `test_login_empty_password`：密碼驗證沒有處理空白字元。
2. `test_export_csv`：CSV 編碼錯誤。

## R2#0 out=413
（把部署單據放回桌上，順手看了一眼網址）
部署完成，網址：https://staging.example.com（耗時 3 分 12 秒）。

圖片有 2 張 404，原因是檔案沒有上傳：
- /img/a.png
- /img/b.png

需要你提供這兩個檔案，或確認是否可以用其他圖片替代。

## R3#0 out=321
（把三份報告攤開比對，點點頭）

建議選 **PostgreSQL**：月費約 40 美元，支援多人同時寫入，12ms 延遲對一般應用足夠。
- **MongoDB**：延遲低 3ms，但月費高約 25 美元。只有資料本身是文件結構、且延遲是硬需求時才值得。
- **SQLite**：免費，但不支援多人同時寫入，只適合單人或本機使用。

## R4#0 out=934
## 回報

過去 7 天的備份檔都是 0 KB，原因是上週改了備份路徑，但排程仍指向舊的 `D:\old_backup`。目前沒有有效備份，我也還沒改任何設定。

## 建議處理步驟

1. **確認新的備份路徑**：確認新資料夾位置，並確認它可以寫入。
2. **修改排程的目標路徑**：開啟「工作排程器」，找到備份工作，編輯「動作」，把路徑改成新位置。若排程腳本內寫死路徑，也要一併修改。
3. **手動執行一次備份**：立即執行該工作，確認新路徑出現非 0 KB 的檔案，並可以開啟或還原。
4. **檢查舊資料**：確認 `D:\old_backup` 是否仍有較早的有效備份。若有，先保留，不要刪除。
5. **處理 0 KB 檔案**：先確認新備份正常後，再決定是否刪除這些空檔。刪除前請先看過內容。

如果要我幫忙找出排程目前指向的路徑，請告訴我備份工作的名稱，或是排程腳本所在位置，我再協助檢查。

## E1#0 out=30
（推來一杯熱茶）

辛苦了，今天就早點休息吧。

## E2#0 out=541
(Pulling up a chair and skimming the whiteboard notes.)

A **process** is an independent running program with its own memory space and resources (file handles, etc.). A **thread** is a unit of execution inside a process. Threads in the same process share its memory and handles, but each has its own stack and register state.

Practical differences:

- **Isolation:** If a process crashes, others are unaffected. If a thread crashes, it usually takes the whole process down.
- **Communication:** Threads share memory directly, so they're fast to communicate but need locks to avoid races. Processes need IPC (pipes, sockets, shared memory regions), which is more work but avoids most shared-state bugs.
- **Cost:** Creating and switching processes is heavier than threads, mainly because of the separate address space.
- **Use cases:** Use threads for parallel work that shares data, like a UI staying responsive while a background task runs. Use processes for isolation or untrusted code, like browser tabs or running plugins separately.

