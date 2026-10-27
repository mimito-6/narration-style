## C1#0 out=55
（放下包包，靠在椅背上嘆氣）

辛苦了，今天的班真的很累。躺下來休息就好，不用急著想什麼。

## C2#0 out=292
（貓盯著牆壁看，多半不是看到鬼。）

最常見的原因：
1. **聽到聲音**：水管、暖氣、牆內老鼠或蟲子、鄰居走動，貓的聽力遠比人敏銳。
2. **看到光影或小動物**：陽光移動、反光、蜘蛛、壁虎、小蟲在牆面爬。
3. **單純發呆或警戒**：貓本來就常長時間凝視某處，尤其是視線高度有窗戶或通道的地方。

如果想確認，可以：
- 去牆壁那邊聽聽看有沒有聲音
- 檢查牆面、踢腳線附近有沒有蟲或小洞

若貓同時出現食慾改變、一直叫、走路異常或突然攻擊空氣等情況，建議找獸醫看看。

## C3#0 out=273
（翻出台北地圖，列出幾個安靜去處）

1. **台北植物園**（士林／大安）：早上人少，有溫室與池塘，適合慢慢散步。
2. **大稻埕河濱公園**：沿河步道寬敞，傍晚可看淡水河與夕陽。
3. **陽明山冷水坑、竹子湖一帶**：山路與步道較清幽，週末建議早點出發，避開車潮。
4. **貓空（木柵）茶園步道**：山上茶園視野好，搭纜車或步行皆可，平日更安靜。
5. **二二八和平公園周邊**：市中心綠地，閒逛與拍照方便。

週末人潮多，若想更安靜，建議清晨前往，並避開假日下午的熱門景點。

## C4#0 out=182
（放下筷子認真想一下）

兩者都不錯，看你要哪種：

- **蛋餅**：蛋白質和油脂較多，比較有飽足感，但通常較油、鈉也高。
- **飯糰**：碳水為主，升糖較快，若選糙米或雜糧、配蛋或豆製品會更均衡。

想要健康一點，選飯糰（糙米或雜糧）加一顆水煮蛋；想吃飽耐餓、上午不易餓，選蛋餅、少加醬。

## S1#0 out=945
（把兩組失敗數據攤開比對）

失敗通常是流程或變因造成，不代表你沒能力。建議依序檢查：

1. 確認對照組狀態：若對照組也異常，多半是試劑、儀器或操作流程的問題；若對照組正常，才是實驗條件本身的問題。
2. 查批次與校正：試劑批號、儀器校正日期、樣本保存時間是否與前次成功時不同。
3. 同條件重做一次：確認失敗是否可重現，排除偶然誤差。
4. 一次只改一個變因：縮小範圍，每次記錄結果。
5. 完整記錄失敗：日期、條件、結果、觀察到的異常，之後寫進實驗紀錄或報告，負結果本身也有參考價值。
6. 拿著數據找師姐討論：把比對表和失敗紀錄帶過去，會比「整個做不出來」更容易找到原因。

## S2#0 out=724
（把履歷網站分頁先關掉）

連續被刷十次，任何人都會累，想放棄是這種階段很自然的感受。

這不代表你的能力不夠。面試結果常受職缺條件、競爭人數和時機影響，很多時候與個人表現無關。

## S3#0 out=661
（放下手機，先別急著再傳）

1. **先別連發訊息。** 三天沒回通常是需要時間冷靜，不一定代表她已放棄這段友誼。
2. **想清楚自己的部分。** 寫下你在意的是什麼，以及你想說的話。
3. **發一則簡短、不施壓的訊息**，例如：「那天我的話說得不太好，對不起。你不用馬上回，我等你準備好。」
4. **之後給她一段時間**，例如一週，期間不要追問「你為什麼不理我」。
5. **若仍無回應**，可以另外約時間當面或通話談。
6. **若她明確表示不想聯絡**，就尊重她的決定。

## S4#0 out=652
（放下滑鼠，靠回椅背）

被當眾罵的當下，人很容易把「這次做砸」直接變成「我不適合待這裡」。辭職這件事先擱著，今天不決定。

1. 把報告哪裡出錯寫成三行，只寫事實，不寫人格評價。
2. 隔天找主管，講你會怎麼修正，這通常比辭職更能扭轉處境。

## T1#0 out=453
（翻開筆記本對照兩者的特性）

**核心差異**

| 項目 | TCP | UDP |
|---|---|---|
| 連線 | 面向連線，需三次握手 | 無連線，直接送 |
| 可靠性 | 保證送達、順序正確、有重傳 | 不保證送達或順序 |
| 流量／壅塞控制 | 有 | 無 |
| 標頭大小 | 較大（至少 20 bytes） | 較小（固定 8 bytes） |
| 傳輸單位 | 位元組串流 | 獨立的資料報（datagram） |
| 延遲 | 較高（握手、重傳、等待順序） | 較低 |

**什麼時候用哪個**

使用 TCP：
- 資料不能遺失或錯序，例如網頁（HTTP/HTTPS）、電子郵件、檔案傳輸（FTP、SFTP）、SSH
- 傳輸量大、要求完整性，而非即時性

使用 UDP：
- 即時性比完整性重要，例如線上遊戲、VoIP、視訊通話、直播
- 本身會容忍少量遺失，例如 DNS 查詢
- 需要廣播或多播
- 協定想自行實作可靠機制，例如 QUIC（HTTP/3 底層）

## T2#0 out=636
（翻出兩種整合方式的差異）

**merge**：把兩條分支的末端接在一起，產生一個有兩個父節點的合併提交（merge commit）。原有歷史保留，分支拓樸可見。
```
git checkout main
git merge feature
```

**rebase**：把你的分支提交「搬」到目標分支最新提交之後，逐一重播，產生新的提交雜湊。歷史呈現為一條直線。
```
git checkout feature
git rebase main
```

**主要取捨**
- 安全性：merge 不改寫既有提交；rebase 會改寫，已推送且他人在用的分支不要 rebase。
- 歷史：merge 保留真實的開發順序；rebase 讓紀錄較乾淨、線性。
- 衝突：merge 一次解決；rebase 會逐個提交重複解衝突，可用 `git rebase --continue` 繼續，或 `--abort` 放棄。

## T3#0 out=1247
（對照錯誤訊息的行號）

`IndexError` 表示程式存取的索引超出 list 範圍。合法索引是 `0` 到 `len(lst) - 1`，負索引則是 `-len(lst)` 到 `-1`。

常見原因：

1. **空 list 取值**：`items = []` 後直接 `items[0]`。
2. **off-by-one**：`range(len(lst) + 1)` 多跑一次，或 `range(1, len(lst))` 漏掉最後一個元素。
3. **迴圈中修改 list**：一邊迭代一邊 `remove()` 或 `append()`，長度改變導致索引錯位。
4. **解析結果欄位不足**：例如 `line.split(',')[2]`，但該行只有兩欄。
5. **搜尋無結果仍取值**：例如 `re.findall(...)[0]` 沒有匹配時回傳空 list。
6. **命令列參數未檢查**：例如 `sys.argv[1]`，但執行時沒有提供參數。
7. **索引計算錯誤**：例如應用 `len(lst) - 1` 卻寫成 `len(lst)`。

修正方式是在取值前先檢查長度：

```python
items = []
if items:
    print(items[0])
else:
    print("list 是空的")
```

## T4#0 out=307
(解釋概念，不需動工具)

**Image（映像檔）**：唯讀的範本，像「安裝光碟」或「類別（class）」。內含應用程式、函式庫與設定，由多層檔案堆疊而成，靜態存放在本機或 registry（如 Docker Hub）。

**Container（容器）**：image 啟動後的執行實例，像「光碟安裝後跑起來的程式」或「由類別產生的物件」。它在 image 之上加一層可寫層，程式執行、寫檔都發生在這裡；停止或刪除容器不會改動 image。

**關係**：
- 一個 image 可以同時啟動多個 container。
- `docker build` 產生 image，`docker run` 從 image 建立並啟動 container。

**指令對照**：
- `docker images`：列出 image
- `docker ps -a`：列出 container（`-a` 含已停止的）

## P1#0 out=265
（寫下函式，附簡短測試）

```python
def is_palindrome(s: str) -> bool:
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert not is_palindrome("race a car")
    assert is_palindrome("")
    assert is_palindrome("No 'x' in Nixon")
    print("ok")
```

說明：`isalnum()` 過濾非英數字元（含中文等 Unicode 字母數字也會保留，若只想要 ASCII 英數，改用 `c.isascii() and c.isalnum()`）；`lower()` 忽略大小寫。

## P2#0 out=253
（寫好 debounce，附上範例）

```javascript
function debounce(fn, delay) {
  let timer = null;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}
```

使用範例：

```javascript
const onSearch = debounce((query) => {
  console.log('搜尋：', query);
}, 300);

onSearch('a');
onSearch('ab');
onSearch('abc'); // 只有最後一次呼叫會在 300ms 後執行：搜尋： abc
```

每次呼叫都會清除前一個計時器，只有停止呼叫滿 `delay` 毫秒後，`fn` 才會執行一次。

## P3#0 out=273
（寫下最常見的寫法：子查詢配 MAX，再回拉員工列）

```sql
SELECT e.id, e.name, e.dept, e.salary
FROM employees e
JOIN (
    SELECT dept, MAX(salary) AS max_salary
    FROM employees
    GROUP BY dept
) m ON e.dept = m.dept AND e.salary = m.max_salary;
```

同薪並列時會全部列出。若只要每部門一人，改用視窗函數：

```sql
SELECT id, name, dept, salary
FROM (
    SELECT id, name, dept, salary,
           ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC) AS rn
    FROM employees
) t
WHERE rn = 1;
```

## P4#0 out=131
（打開終端機準備執行統計）

Windows 環境是 PowerShell，用這行即可（遞迴搜尋，含子資料夾）：

```powershell
(Get-ChildItem -Recurse -Filter *.log -File | Get-Content | Measure-Object).Count
```

若只要目前資料夾、不含子資料夾，去掉 `-Recurse`。

## R1#0 out=151
（對照測試輸出，整理失敗原因）

測試結果：128 通過、2 失敗。

1. `test_login_empty_password`：密碼驗證沒有處理空白字元。純空白（如 `"   "`）被當成有效密碼，未被拒絕。
2. `test_export_csv`：CSV 編碼錯誤。

尚未修改任何程式碼。兩者都可以直接修，要我開始處理嗎？

## R2#0 out=106
（回報部署結果）

部署完成：https://staging.example.com（耗時 3 分 12 秒）

有 2 張圖片 404，原因是檔案未上傳：
- /img/a.png
- /img/b.png

需要補上這兩個檔案後重新部署。要我繼續處理嗎？

## R3#0 out=550
（整理三方案結果，給出建議）

**建議：PostgreSQL**

- **多人同時寫入**：PostgreSQL 支援，SQLite 不支援，這點直接排除 SQLite。
- **延遲**：PostgreSQL 12ms、MongoDB 9ms，差 3ms，對多數應用影響很小。
- **成本**：PostgreSQL 月費約 40 美元，比 MongoDB 的 65 美元便宜約 25 美元/月。

若資料本身是文件型結構、且讀寫模式以文件為主，才考慮 MongoDB。

## R4#0 out=883
（查到排程仍指向舊路徑，已對照完畢）

過去 7 天的備份全是 0 KB，原因是上週改了備份路徑，但排程仍寫著 `D:\old_backup`。我還沒改任何設定。

修正步驟：
1. 開啟「工作排程器」，找到這個備份工作，點右鍵「內容」。
2. 切到「動作」，選取現有動作後按「編輯」。
3. 把「起始於」或程式引數中的 `D:\old_backup` 改成新的備份路徑，按「確定」。
4. 右鍵該工作選「執行」，確認新產生的備份檔大小不是 0 KB。

注意：舊的 0 KB 檔案未被刪除。這 7 天的資料沒有備份成功，若需要復原，要從來源重新備份。

## E1#0 out=31
（放下包包，靠到椅背上）

辛苦了，今天先好好休息。

## E2#0 out=702
(Opens Task Manager and checks the thread count)

- **Process:** a running program with its own private memory, file handles, and resources. The OS isolates processes, so one crashing rarely takes down another. Creating one is relatively expensive, and processes talk through IPC (pipes, sockets, shared memory).
- **Thread:** an execution path inside a process. Threads in the same process share its memory and handles, each with its own stack and registers. Creating and switching threads is cheap, but shared data needs locks, or you get race conditions.

**Practical rule:**
- Use **processes** when you need isolation or crash safety, such as browser tabs or running untrusted plugins.
- Use **threads** when work needs to share data quickly, such as a server handling requests against one in-memory cache, or a GUI keeping the UI responsive during a long task.

