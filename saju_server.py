from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

@app.route('/api/saju', methods=['POST'])
def saju():
    data = request.get_json()
    year = data['year']
    month = data['month']
    day = data['day']
    hour = data['hour']
    gender = data['gender']

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://chunmyung.com/saju")

    # TODO: 여기에 크롤링 로직 삽입
    result = "크롤링된 사주 결과 (예시)"

    driver.quit()
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
