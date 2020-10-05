mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = 8051\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml