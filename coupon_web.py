import streamlit as st

st.title("クーポン併用チェッカー")

rules = {
    frozenset(["100円引き", "商品券"]): (
        "○ 併用できます",
        "商品券と100円引きクーポンは併用可能です。"
    ),
    frozenset(["100円引き", "コーン増量"]): (
        "× 併用できません",
        "100円引きクーポンとコーン増量は併用できません。"
    ),
}

coupons = ["100円引き", "商品券", "コーン増量"]

coupon_a = st.selectbox("クーポンA", coupons)
coupon_b = st.selectbox("クーポンB", coupons)

if st.button("併用できるか判定"):
    if coupon_a == coupon_b:
        st.warning("同じものが選択されています")
    else:
        result = rules.get(frozenset([coupon_a, coupon_b]))

        if result:
            message, reason = result

            if message.startswith("○"):
                st.success(message)
            else:
                st.error(message)

            st.write(reason)
        else:
            st.info("△ 判定できません")