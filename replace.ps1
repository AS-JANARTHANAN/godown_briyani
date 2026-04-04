$files = Get-ChildItem -Filter *.html
foreach ($file in $files) {
    (Get-Content $file.FullName -Raw) -replace 'Godown Briyani', 'Bhai Biryani Godown' -replace 'Godown Biryani', 'Bhai Biryani Godown' | Set-Content $file.FullName -NoNewline
}
