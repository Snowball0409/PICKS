var express = require("express");
const axios = require("axios");
const mysql = require("mysql");
var router = express.Router();

router.post("/", async (req, res) => {
    try {
        const userInput = req.body.userInput;

        const azureFunctionUrl =
            "https://pybot-lat.azurewebsites.net/api/HttpTrigger1?code=1iYQHuyKyXXznfScFxiba1Xc-lsHtuBf2l2H2gQkWtHzAzFuHefheg==";

        console.log("Wait for Response...");
        const response = await axios.post(azureFunctionUrl, {
            userInput: userInput,
        });

        const connection = mysql.createConnection({
            host: "hellomysql20230529.mysql.database.azure.com",
            user: "zing",
            password: "Ab123456789",
            database: "test0529",
            ssl: {
                rejectUnauthorized: false,
            },
        });

        const courseList = response.data.Output;
        const courseFound = [];

        const query = "SELECT * FROM `1111` WHERE 中文課程名稱 IN (?)";

        const executeQuery = () => {
            return new Promise((resolve, reject) => {
                connection.query(
                    query,
                    courseList,
                    (error, results, fields) => {
                        if (error) {
                            console.error("執行查詢失敗：", error);
                            reject(error);
                        } else {
                            results.forEach((row) => {
                                courseFound.push(row);
                                console.log(row);
                            });
                            resolve();
                        }
                    }
                );
            });
        };

        connection.connect(async (err) => {
            if (err) {
                console.error("連線失敗：", err);
                return res.status(500).json({ error: "連線失敗" });
            }
            console.log("連線成功！");

            try {
                await executeQuery();
                connection.end();
                // 在这里处理 Azure Function 的回应
                res.json({ output: courseFound });
            } catch (error) {
                connection.end();
                console.error("执行查询失败：", error);
                return res.status(500).json({ error: "执行查询失败" });
            }
        });
    } catch (error) {
        console.error("An error occurred:", error);
        res.status(500).json({ error: "An error occurred" });
    }
});

module.exports = router;
