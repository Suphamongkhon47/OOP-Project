import streamlit as st

st.header('ราคาของสินค้าของ SUPERMARKET',divider='red')
menu = st.sidebar.radio('MENU',['ชำระสินค้าเงินบาท(Pay for products in baht)','ຈ່າຍຄ່າສິນຄ້າເປັນເງິນລາວ(Pay for products in Lao money)'])
def calculate_total_price(price, quantity, discount):
    total_price = (price * quantity) * (1 - discount / 100)
    return total_price

def main():
 if menu == 'ชำระสินค้าเงินบาท(Pay for products in baht)':
     #รูปภาพ
    st.title("ช่องทางการชำระเงินไทย")
    st.image('https://png.pngtree.com/png-vector/20230801/ourmid/pngtree-kawaii-food-vector-illustration-with-kawaii-fruits-and-juices-png-image_6829153.png', width=500)

    st.subheader("รายละเอียดราคาสินค้าและส่วนลดของสินค้า")
    price = st.number_input("ราคาสินค้า (บาท)", min_value=0.0, step=0.01)
    quantity = st.number_input("จำนวนสินค้า", min_value=1, step=1)
    discount = st.number_input("ส่วนลด (%)", min_value=0.0, max_value=100.0, step=1.0)

    if st.button("คำนวณ"):
        total_price = calculate_total_price(price, quantity, discount)
        st.success(f"ราคารวมทั้งหมด: {total_price:.2f} บาท")
 
 if menu == 'ຈ່າຍຄ່າສິນຄ້າເປັນເງິນລາວ(Pay for products in Lao money)':
    st.title("ຊ່ອງທາງການຈ່າຍເງິນຂອງລາວ")
    st.image('https://png.pngtree.com/png-vector/20230801/ourmid/pngtree-kawaii-food-vector-illustration-with-kawaii-fruits-and-juices-png-image_6829153.png', width=500)
    st.subheader("ລາຍລະອຽດຂອງລາຄາສິນຄ້າ ແລະສ່ວນຫຼຸດສິນຄ້າ")
    price = st.number_input("ລາຄາສີນຄ້າ(ราคาสินค้า) (ກີບ) ", min_value=0.0, step=0.01)
    quantity = st.number_input("ຈຳນວນສີນຄ້າ(จำนวนสินค้า)", min_value=1, step=1)
    discount = st.number_input("ສ່ວນຫຼຸດ(ส่วนลด) (%)", min_value=0.0, max_value=100.0, step=1.0)

    if st.button("ຄຳນວນ"):
        total_price_lao = calculate_total_price(price, quantity, discount)
        st.success(f"ລາຄາສິນຄ້າທັງໝົດ: {total_price_lao:.2f} ກີບ")
# เพิ่ม CSS สำหรับจัดภาพอยู่ตรงกลาง
    st.markdown(
    f'<style>div.stImage > img {{display: block; margin-left: auto; margin-right: auto;}}</style>',
    unsafe_allow_html=True
)
def set_background(image_url):
    image_url_str = f'url("{image_url}")'
    css = f"""
    <style>
    .stApp {{
        background-image: {image_url_str};
        background-size: cover;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


##ใช้งานตรงนี้
set_background("https://static.vecteezy.com/system/resources/previews/013/011/166/original/grocery-store-or-supermarket-with-food-product-shelves-racks-dairy-fruits-and-drinks-for-shopping-in-flat-cartoon-hand-drawn-templates-illustration-vector.jpg")
if __name__ == "__main__":
    main()
    

