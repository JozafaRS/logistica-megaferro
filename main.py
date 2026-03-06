import streamlit as st

def main():
    industria = st.Page(
        page="pages/industria.py",
        title="Indústria",
    )
    loja = st.Page(
        page="pages/loja.py",
        title="Loja",
    )

    nav = st.navigation([industria,loja])

    nav.run()

if __name__ == "__main__":
    main()