from stegano import lsb

# Encode message
secret_data = "FUN :) CTF{HELLO $TraNger}"
cover_image = "supermario.png"
steg_image = "new_supermario.png"
lsb.hide(cover_image, secret_data).save(steg_image)

# Decode message
decoded_data = lsb.reveal(steg_image)
print(decoded_data)