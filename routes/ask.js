var express = require("express");
var { spawn } = require("child_process");
var router = express.Router();

router.post("/", (req, res) => {
    // 從請求的 JSON 主體中獲取使用者輸入
    const userInput = req.body.userInput;

    // 使用 spawn 啟動一個 Python 子進程
    const pythonProcess = spawn("python", ["bin/bot.py", userInput]);

    let output = "";

    // 監聽子進程的輸出
    pythonProcess.stdout.on("data", (data) => {
        output += data.toString();
    });

    // 監聽子進程的錯誤訊息
    pythonProcess.stderr.on("data", (data) => {
        console.error(`Python error: ${data}`);
        res.status(500).json({ error: "An error occurred" });
    });

    // 子進程結束時發送回應
    pythonProcess.on("close", (code) => {
        if (code === 0) {
            res.json({ output });
        } else {
            res.status(500).json({ error: "An error occurred" });
        }
    });
});

module.exports = router;
