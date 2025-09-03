# test_api_day3.ps1
# Quick tests for /api/categories, /api/entries, /api/customers, /api/products
# Requirements: Django server running at http://127.0.0.1:8000, user exists.

$BASE = "http://127.0.0.1:8000"
$USERNAME = "admin"
$PASSWORD = "Admin12345"  # <-- заміни на свій пароль

Write-Host "1) Отримую JWT токен..." -ForegroundColor Cyan
$loginBody = @{ username=$USERNAME; password=$PASSWORD } | ConvertTo-Json -Depth 3
$resp = Invoke-RestMethod -Uri "$BASE/auth/jwt/create" -Method Post -ContentType "application/json" -Body $loginBody
$token = $resp.access
if (-not $token) { throw "Не отримано токен. Перевір логін/пароль." }
$headers = @{ Authorization = "Bearer $token" }
Write-Host "OK" -ForegroundColor Green

Write-Host "2) GET списки (categories, entries, customers, products)..." -ForegroundColor Cyan
Invoke-RestMethod -Uri "$BASE/api/categories/" -Headers $headers
Invoke-RestMethod -Uri "$BASE/api/entries/" -Headers $headers
Invoke-RestMethod -Uri "$BASE/api/customers/" -Headers $headers
Invoke-RestMethod -Uri "$BASE/api/products/" -Headers $headers
Write-Host "OK" -ForegroundColor Green

Write-Host "3) Створюю category з кирилицею (UTF-8 байтами)..." -ForegroundColor Cyan
$catJson = @{ name="Робота"; color="#2b8a3e" } | ConvertTo-Json -Depth 5 -Compress
$catBytes = [System.Text.Encoding]::UTF8.GetBytes($catJson)
Invoke-RestMethod -Uri "$BASE/api/categories/" -Method Post -Headers $headers -ContentType "application/json; charset=utf-8" -Body $catBytes
Write-Host "OK" -ForegroundColor Green

Write-Host "4) Перевіряю categories знову..." -ForegroundColor Cyan
Invoke-RestMethod -Uri "$BASE/api/categories/" -Headers $headers | Format-Table -AutoSize
Write-Host "OK" -ForegroundColor Green

Write-Host "5) Створюю product та customer (потрібна активна організація!)..." -ForegroundColor Cyan
# УВАГА: якщо немає Membership для користувача, отримаєш 403 "No active organization".
# Створи Organization і Membership у /admin (зв'яжи користувача з організацією).

# product
$prodJson = @{ sku="SKU-100"; name="Товар 100"; price=199.99; category="Основні" } | ConvertTo-Json -Depth 5 -Compress
$prodBytes = [System.Text.Encoding]::UTF8.GetBytes($prodJson)
try {
  Invoke-RestMethod -Uri "$BASE/api/products/" -Method Post -Headers $headers -ContentType "application/json; charset=utf-8" -Body $prodBytes
} catch {
  Write-Warning "Products POST помилка: $($_.Exception.Message)"
}

# customer
$custJson = @{ name="ТОВ Ромашка"; email="romashka@example.com"; phone="+380000000000" } | ConvertTo-Json -Depth 5 -Compress
$custBytes = [System.Text.Encoding]::UTF8.GetBytes($custJson)
try {
  Invoke-RestMethod -Uri "$BASE/api/customers/" -Method Post -Headers $headers -ContentType "application/json; charset=utf-8" -Body $custBytes
} catch {
  Write-Warning "Customers POST помилка: $($_.Exception.Message)"
}

Write-Host "6) GET customers/products після створення..." -ForegroundColor Cyan
Invoke-RestMethod -Uri "$BASE/api/customers/" -Headers $headers | Format-Table -AutoSize
Invoke-RestMethod -Uri "$BASE/api/products/" -Headers $headers | Format-Table -AutoSize
Write-Host "Готово." -ForegroundColor Green
