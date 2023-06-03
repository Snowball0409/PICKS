const express = require("express");
const axios = require("axios");
const router = express.Router();

router.post("/", async (req, res) => {
    try {
        // 從請求的 JSON 主體中獲取使用者輸入
        const userInput = req.body.userInput;

        // 設定 Azure Function 的 URL
        const azureFunctionUrl =
            "https://pybot-lat.azurewebsites.net/api/HttpTrigger1?code=Nh7R7ViwrpYfsfgvL37FPcfO20CpPaDG4g5nid_7ZjeuAzFu1cX9bw==";

        // 發送 HTTP POST 請求給 Azure Function
        const response = await axios.post(azureFunctionUrl, { userInput });

        // 在這裡處理 Azure Function 的回應
        res.json({ output: response.data });
    } catch (error) {
        console.error("An error occurred:", error);
        res.status(500).json({ error: "An error occurred" });
    }
});

module.exports = router;
