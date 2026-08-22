from django import forms

from core.forms.base import FormControlMixin
from core.models.brand import School
from core.utilities.helpers import set_placeholders


class SchoolForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = School
        fields = [
            "name",
            "address",
            "phone",
            "email",
            "website",
            "logo",
            "npsn",
            "nss",
            "school_type",
            "school_status",
            "accreditation",
            "curriculum",
            "headmaster_name",
            "headmaster_nip",
            "established_year",
            "district",
            "city",
            "province",
            "village",
            "postal_code",
            "motto",
            "vision",
            "mission",
            "goals",
        ]
        widgets = {
            "address": forms.Textarea(attrs={"rows": 3}),
            "vision": forms.Textarea(attrs={"rows": 3}),
            "mission": forms.Textarea(attrs={"rows": 3}),
            "goals": forms.Textarea(attrs={"rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        set_placeholders(
            self,
            {
                "name": "Nama sekolah",
                "address": "Alamat sekolah",
                "phone": "Telepon",
                "email": "Email sekolah",
                "website": "https://example.com",
                "logo": "https://example.com/logo.png",
                "npsn": "NPSN",
                "nss": "NSS",
                "school_type": "Jenjang",
                "school_status": "Negeri/Swasta",
                "accreditation": "Akreditasi",
                "curriculum": "Kurikulum",
                "headmaster_name": "Nama kepala sekolah",
                "headmaster_nip": "NIP",
                "established_year": "Tahun berdiri",
                "district": "Kecamatan",
                "city": "Kota",
                "province": "Provinsi",
                "village": "Kelurahan",
                "postal_code": "Kode pos",
                "motto": "Motto",
                "vision": "Visi",
                "mission": "Misi",
                "goals": "Tujuan",
            },
        )
