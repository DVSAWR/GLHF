# JWT

```unix
ssh-keygen -t rsa -b 2048
```

JSON Web Token (JWT) - это JSON-объект, который определен в открытом стандарте RFC 7519. Он считается одним из безопасных способов передачи информации между двумя участниками.

Для его создания нужно определить:

- Заголовок (header)
- Полезную нагрузку (payload)
- Подписи (signature)

Простыми словами, JWT - это строка в формате:

`header.payload.signature`

## HEADER

Заголовок JWT содержит информацию, как должна вычисляться JWT-подпись. Это тоже JSON-объект, который выглядит так:

`header = {"alg": "HS256", "typ": "JWT"}`

- typ (type) означет, что это JWT
- alg (algorithm) определяет алгоритм хеширования, который будет использоваться при генерации подписи.

HS256 - HMAC-SHA256 (тип хеширования), для его вычисления нужен один секретный ключ. Можно использорвать RS256 - он ассиметричный и создает 2 ключа: публичный и правтный. С помощью приватного создается подпись, а с помощью публичного проверяется подлинность подписи.

## PAYLOAD

Payload - это полезные данные, которые храняться в JWT. Эти данные называются JWT-claims.
В нашем примере payload содержит информацию об id пользователя:

`payload = {"userid": "b08f86af-35da-48f2-8fab-cef3904660bd"}`

Можно положить в payload сколько угодно claims

список стандартных claims:

    - iss (issuer) - изнадель токена
    - sub (subject) - тема токена
    - exp (expiration time) - время жизни токена
    - aud (audience) - получатели токена
    - nbf (not before) - срок, до которого токен не действителен
    - iat (issued at) - время издание токена
    - jti (JWT id) - идентификатор токена

## SIGNATURE

Подпись вычисляется с использованием слудющего псевдо-кода:

```
const SECRET_KEY = ''
const unsignedToken = base64urlEncode(header) + '.' + base64urlEncode(payload)
const signature = HMAC-SHA256(unsignedToken, SECRET_KEY)
```

Алгоритм base64url кодирует header и payload, созданные на 1 и 2 шаге.

Алгоритм соединяется закодированные строки через точку. Затем полученная строка хешируется алгоритмом, заданным в header на основе нашего секретного ключа.

## IMPLEMENTATION

```python
def base64url_encode(item):
        return urlsafe_b64encode(item).rstrip(b'=')


def base64url_decode(item):
    equal_sign_count = len(item) % 4
    if equal_sign_count:
        item += b'=' * equal_sign_count
    return urlsafe_b64decode(item)


def jwt_token_create(payload, secret_key):
    header = {
        'alg': 'HS256',
        'typ': 'JWT'
    }
    header_encoded = base64url_encode(json.dumps(header).encode('utf-8'))
    payload_encoded = base64url_encode(json.dumps(payload).encode('utf-8'))
    signature = hmac.new(secret_key.encode('utf-8'), header_encoded + b'.' + payload_encoded, hashlib.sha256).digest()
    signature_encoded = base64url_encode(signature)
    jwt_token = header_encoded + b'.' + payload_encoded + b'.' + signature_encoded
    return jwt_token.decode('utf-8')


def jwt_toke_decode(jwt_token, secret_key):
    header_encoded, payload_encoded, signature_encoded = jwt_token.encode('utf-8').split(b'.')
    signature_validation = hmac.new(secret_key.encode('utf-8'), header_encoded + b'.' + payload_encoded, hashlib.sha256).digest()
    if base64url_encode(signature_validation) != signature_encoded:
        return 'ERROR WRONG SIGNATURE'
    payload_decoded = base64url_decode(payload_encoded)
    return json.loads(payload_decoded)
  ```
