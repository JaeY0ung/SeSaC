import hashlib
import time
# 데이터베이스 연결
    
def hash_password(): #1120, 2240,  
    jongkyung_hash_phoneNum = 'AB47D3670A455613CD16B40002E1D46593255D39E23B9EDC5CA9DC1D67D84310'.lower()
    for i in range(2240,10000):
        for j in range(0,10000):
            predict_phoneNum = f'010{i:04d}{j:04d}'
            hash_predict_phoneNum = hashlib.sha256(predict_phoneNum.encode()).hexdigest()
            print(f'010{i:04d}{j:04d} SHA256 암호 -> {hash_predict_phoneNum}')
            if hash_predict_phoneNum == jongkyung_hash_phoneNum:
                return f"종경이 번호: {predict_phoneNum}"
print(hash_password())