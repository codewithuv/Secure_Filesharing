from django.core.signing import Signer
signer = Signer()

# Encrypt
signed_url = signer.sign(f"/api/download/{file_id}/")

# Decrypt in download view and verify user type
original_path = signer.unsign(signed_url)
