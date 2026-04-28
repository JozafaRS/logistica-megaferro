import streamlit as st

def main():
    # industria = st.Page(
    #     page="pages/industria.py",
    #     title="Indústria",
    # )
    # loja = st.Page(
    #     page="pages/loja.py",
    #     title="Loja",
    # )

    logistica = st.Page(
        page="pages/logistica.py",
        title="Logística Megaferro"
    )

    nav = st.navigation([logistica])

    nav.run()

if __name__ == "__main__":
    main()