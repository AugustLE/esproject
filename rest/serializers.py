from rest_framework import serializers

from homepage.models import CheckList, Question, Option, ChecklistAnswer, Answer
from user.models import CustomUser
from rest_framework.response import Response
from rest_framework import status

class OptionSerializer(serializers.ModelSerializer):

    question_id = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all(), source='question.pk')

    class Meta:

        model = Option
        fields = ('question_id', 'optionText', 'solution')

class QuestionSerializer(serializers.ModelSerializer):

    checklist_id = serializers.PrimaryKeyRelatedField(queryset=CheckList.objects.all(), source='checkList.pk')
    options = OptionSerializer(many=True)

    class Meta:

        model = Question
        fields = ('pk', 'checklist_id', 'question_text', 'isOptions', 'priority', 'options')

    """def create(self, validated_data):
        
        subject = Question.objects.create()"""



class ChecklistSerializer(serializers.ModelSerializer):

    questions = QuestionSerializer(many=True)

    class Meta:
        model = CheckList
        fields = ('pk', 'name', 'is_front', 'questions')
        #fields = '__all__'



class AnswerSerializer(serializers.ModelSerializer):

    checklist_answer_id = serializers.PrimaryKeyRelatedField(queryset=ChecklistAnswer.objects.all(), source='answerChecklist.pk')

    class Meta:

        model = Answer
        fields = ('checklist_answer_id','answerText', 'question', 'option')



class ChecklistAnswerSerializer(serializers.ModelSerializer):

    answers = AnswerSerializer(many=True)
    checklist_name = serializers.PrimaryKeyRelatedField(queryset=CheckList.objects.all(),
                                                             source='checklist.name', required=False)
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:

        model = ChecklistAnswer
        fields = ('owner', 'pk', 'checklist_name', 'answer_email', 'checklist', 'date_sent', 'answers')

    def create(self, validated_data):

        print(validated_data)
        answer_data = validated_data.pop('answers')
        ch_answer = ChecklistAnswer.objects.create(**validated_data)

        for answer in answer_data:
            Answer.objects.create(answerChecklist=ch_answer, **answer)
        return ch_answer

class UserSerializer(serializers.ModelSerializer):

    answers = serializers.PrimaryKeyRelatedField(many=True, queryset=ChecklistAnswer.objects.all())

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'answers')











