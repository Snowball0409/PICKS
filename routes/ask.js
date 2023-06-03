var express = require("express");
var { spawn } = require("child_process");
var iconv = require("iconv-lite");
var axios = require("axios");
var router = express.Router();

router.post("/", (req, res) => {
    // 從請求的 JSON 主體中獲取使用者輸入
    const userInput = req.body.userInput;

    // 設定容器的 IP 位址和端口號
    const containerUrl =
        "https://pybot.internal.bravesky-7a2be4de.centralus.azurecontainerapps.io:3000";

    // 發送 HTTP POST 請求給容器
    axios
        .post(containerUrl, userInput)
        .then((response) => {
            // 在這裡處理容器的回應
            res.json({ output: response.data });
        })
        .catch((error) => {
            console.error("An error occurred:", error);
            res.status(500).json({ error: "An error occurred" });
        });
});

module.exports = router;
