
from django.shortcuts import render


def home(request):

    zprava = ""

    if request.method == "POST":

        pohlavi = request.POST.get("pohlavi")
        vek = request.POST.get("vek")

        if pohlavi and vek:

            try:
                vek = int(vek)

                if vek < 0 or vek > 120:
                    zprava = "Zadej platný věk!"

                else:
                    zprava = f"Jsi {pohlavi} a je ti {vek} let!"

            except ValueError:
                zprava = "Zadej platný věk!"

    return render(request, "formular/home.html", {
        "zprava": zprava
    })
