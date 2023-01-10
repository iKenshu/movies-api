from rest_framework import serializers


def validate_password_strenght(password):
    if password.upper() == password:
        print(password)
        raise serializers.ValidationError(
            {"password": "Password must contain at least 1 lower case letter."}
        )
    if password.lower() == password:
        raise serializers.ValidationError(
            {"password": "Password must contain at least 1 upper case letter."}
        )

    if not any(char in ["@", "?", "!", "#", "]"] for char in password):
        raise serializers.ValidationError(
            {
                "password": "Password must contain at least one of these special characters @, ?, !,#, ]."
            }
        )
    return password
