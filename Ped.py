import webbrowser

urls = ["http://www.google.com", "http://www.facebook.com"]

def main():
    for url in urls:
        input(f"Presiona Enter para abrir {url} en el navegador...")
        webbrowser.open(url)

if __name__ == "__main__":
    main()
