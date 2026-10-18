# Reporting Dashboard Starter

A beginner-friendly Streamlit dashboard starter with:
- CSV / Excel upload
- Search across columns
- Basic metrics and charts
- Download filtered rows
- WhatsApp contact link
- Mobile-responsive Streamlit layout

## Important security note
The included username/password is a demonstration only. It is not secure authentication and must not be used for confidential information. Anyone who can access the app source can discover the demo credentials. Do not upload customer-identifiable, insurance, financial, or other confidential data to this starter app.

For a real admin/user system with private data, use a proper authentication provider and a database with server-side access controls. Do not store passwords in a CSV, source code, or browser JavaScript.

## Run locally
1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Install packages: `pip install -r requirements.txt`
4. Start: `streamlit run app.py`

## Deploy using Streamlit Community Cloud
1. Create a GitHub account at https://github.com/
2. Create a **private** repository if the source should not be public.
3. Upload `app.py`, `requirements.txt`, and `README.md`.
4. Open https://share.streamlit.io/ and sign in with GitHub.
5. Create/deploy an app and select the repository, branch `main`, and file `app.py`.
6. Deploy. Streamlit will provide a hosted `streamlit.app` address if deployment succeeds.

Free plans and deployment availability may change. A private repository does not automatically make the deployed app private. Configure app access/authentication separately before using private data.

## Customize
- Change the demo WhatsApp link near the bottom of `app.py`.
- Replace the sample data with your own report by uploading a CSV or Excel file.
- Add production authentication and a database before using this for multiple real users.
