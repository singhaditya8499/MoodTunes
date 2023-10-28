from django.shortcuts import render
from django.http import HttpResponse

def ham_a_questionnaire(request):

    # Define the questions and their respective weights.
        questions = [
            ("Anxious mood", 1),
            ("Tension", 1),
            ("Fears", 1),
            ("Insomnia", 1),
            ("Intellectual", 1),
            ("Depressed mood", 1),
            ("Somatic (muscular)", 1),
            ("Somatic (sensory)", 1),
            ("Cardiovascular symptoms", 1),
            ("Respiratory symptoms", 1),
            ("Gastrointestinal symptoms", 1),
            ("Genitourinary symptoms", 1),
            ("Autonomic symptoms", 1),
            ("Behavior at interview", 1)
        ]

        if request.method == "POST":
            # Process the form submission
            total_score = 0

            for question, weight in questions:
                response = int(request.POST.get(question, 0))
                total_score += response * weight

            # Calculate the total HAM-A score.
            ham_a_score = total_score
            percentage_score = (ham_a_score / 56) * 100

            if percentage_score <= 30:
                interpretation = "Low Anxiety"
            elif percentage_score <= 60:
                interpretation = "Moderate Anxiety"
            else:
                interpretation = "High Anxiety"

            return render(request, 'ham_a_app/result.html', {'percentage_score': percentage_score, 'interpretation': interpretation})

        return render(request, 'ham_a_app/questionnaire.html', {'questions': questions})
