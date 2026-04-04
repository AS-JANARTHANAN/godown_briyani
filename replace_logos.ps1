$files = Get-ChildItem -Filter *.html
foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw
    
    # Favicon
    $content = $content -replace 'href="images/logo\.webp"', 'href="images/bbg-logo-filled.png"'
    
    # Nav logo
    $content = [regex]::Replace($content, 'src="images/logo\.webp"\s+alt="?[^"]*"?\s+class="nav-logo"', 'src="images/bbg-logo-outline.png" alt="Bhai Biryani Godown logo — Since 1977 Trichy" class="nav-logo"')
    
    # Footer logo
    $content = [regex]::Replace($content, 'src="images/logo\.webp"\s+alt="?[^"]*"?\s+class="footer-logo"', 'src="images/bbg-logo-filled.png" alt="Bhai Biryani Godown logo — Since 1977 Trichy" class="footer-logo"')
    
    # Hero logo in index.html and any other stray logos
    $content = [regex]::Replace($content, 'src="images/logo\.webp"', 'src="images/bbg-logo-outline.png"')

    Set-Content $file.FullName $content -NoNewline
}
