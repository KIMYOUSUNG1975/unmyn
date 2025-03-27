// 달빛천사의운명노트 - 전문가형 사주풀이 React 앱
import React, { useState } from 'react';
import axios from 'axios';

export default function App() {
  const [birthDate, setBirthDate] = useState('');
  const [birthTime, setBirthTime] = useState('');
  const [gender, setGender] = useState('여자');
  const [result, setResult] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);
    setResult('');

    const prompt = `사용자의 생년월일: ${birthDate}\n태어난 시간: ${birthTime}\n성별: ${gender}\n위 정보를 바탕으로 전문가처럼 분석적인 사주 풀이를 해줘. 항목: 성격 및 성향, 직업운, 연애운, 재물운. 문체는 전문적인 어투로.`;

    try {
      const response = await axios.post(
        'https://api.openai.com/v1/chat/completions',
        {
          model: 'gpt-3.5-turbo',
          messages: [{ role: 'user', content: prompt }]
        },
        {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer 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' // ← 여기만 수정하세요!
          }
        }
      );

      setResult(response.data.choices[0].message.content);
    } catch (error) {
      console.error(error);
      if (error.response?.status === 401) {
        setResult('❌ API 인증 오류입니다. 올바른 OpenAI API 키를 사용하고 있는지 확인해주세요.');
      } else if (error.response?.status === 429) {
        setResult('🚫 요청이 너무 많습니다. 잠시 후 다시 시도해주세요.');
      } else {
        setResult('오류가 발생했습니다. 다시 시도해주세요.');
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-4">
      <div className="bg-white p-6 rounded-2xl shadow-xl w-full max-w-xl">
        <h1 className="text-2xl font-bold mb-4 text-center">🌙 달빛천사의운명노트</h1>

        <div className="space-y-4">
          <label>
            생년월일
            <input
              type="date"
              className="w-full border p-2 rounded"
              value={birthDate}
              onChange={(e) => setBirthDate(e.target.value)}
              required
            />
          </label>

          <label>
            태어난 시간
            <input
              type="text"
              placeholder="예: 오전 3시"
              className="w-full border p-2 rounded"
              value={birthTime}
              onChange={(e) => setBirthTime(e.target.value)}
              required
            />
          </label>

          <label>
            성별
            <select
              className="w-full border p-2 rounded"
              value={gender}
              onChange={(e) => setGender(e.target.value)}
              required
            >
              <option value="여자">여자</option>
              <option value="남자">남자</option>
            </select>
          </label>

          <button
            onClick={handleSubmit}
            disabled={loading}
            className="w-full bg-purple-500 text-white py-2 rounded-xl hover:bg-purple-600"
          >
            {loading ? '풀이 중...' : '🔮 사주풀이 보기'}
          </button>
        </div>

        {result && (
          <div className="mt-6 whitespace-pre-wrap bg-gray-50 p-4 rounded-xl border">
            {result}
          </div>
        )}
      </div>
    </div>
  );
}
