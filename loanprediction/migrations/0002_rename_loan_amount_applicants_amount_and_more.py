# Generated by Django 4.0.3 on 2022-03-20 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loanprediction', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicants',
            old_name='Loan_Amount',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='applicants',
            old_name='Approved',
            new_name='approved',
        ),
        migrations.RenameField(
            model_name='applicants',
            old_name='Coapplicant_income',
            new_name='coapplicant',
        ),
        migrations.RenameField(
            model_name='applicants',
            old_name='Dependents',
            new_name='dependents',
        ),
        migrations.RenameField(
            model_name='applicants',
            old_name='Education',
            new_name='education',
        ),
        migrations.RenameField(
            model_name='applicants',
            old_name='Employment',
            new_name='employment',
        ),
        migrations.RenameField(
            model_name='applicants',
            old_name='Income',
            new_name='income',
        ),
        migrations.RenameField(
            model_name='applicants',
            old_name='Loan_term',
            new_name='loan_term',
        ),
    ]
