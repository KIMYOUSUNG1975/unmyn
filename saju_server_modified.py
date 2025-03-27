from flask import Flask, request, jsonify
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)
CORS(app)  # CORS 허용 추가

@app.route('/api/saju', methods=['POST'])
def saju():
    data = request.get_json()
    year = data['year']
    month = data['month']
    day = data['day']
    hour = data['hour']
    gender = data['gender']

    # 현재는 실제 크롤링 로직 없이 임시 결과 생성
    result = f"🔮 {year}년 {month}월 {day}일 {hour}시에 태어난 {gender}님의 사주 결과입니다. (예시 데이터)"

    # 향후: Selenium 또는 실제 사주 분석 로직 삽입 가능
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
