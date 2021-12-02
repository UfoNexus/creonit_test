from rest_framework import serializers

from .models import Answer, Question, Quiz


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = [
            'id', 'quiz', 'text', 'order', 'answers'
        ]

    def update(self, instance, validated_data):
        answers_data = validated_data.pop('answers')
        current_answers = instance.answers.all()
        current_answers = list(current_answers)
        instance.text = validated_data.get('text', instance.text)
        instance.order = validated_data.get('order', instance.order)
        instance.save()

        for answers in answers_data:
            answer = current_answers.pop(0)
            answer.text = answers.get('text', answer.text)
            answer.is_correct = answers.get('is_correct', answer.is_correct)
            answer.save()
        return instance


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = [
            'id', 'title', 'slug', 'questions_count', 'description',
            'creation_date', 'is_active', 'questions'
        ]

    def create_answers(self, answer_data):
        question = answer_data.get('question')
        text = answer_data.get('text')
        is_correct = answer_data.get('is_correct')
        Answer.objects.create(question=question,
                              text=text,
                              is_correct=is_correct)
        return

    def create_question(self, questions_data):
        quiz = questions_data.get('quiz')
        text = questions_data.get('text')
        order = questions_data.get('order')
        new_question = Question.objects.create(quiz=quiz,
                                               text=text,
                                               order=order)
        new_question.save()
        # answers_dict = questions_data.get('answers')
        # for answer in answers_dict:
        #     self.create_answers(answer)
        return

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.questions_count = validated_data.get(
            'questions_count', instance.questions_count
        )
        instance.description = validated_data.get(
            'description', instance.description
        )
        instance.is_active = validated_data.get(
            'is_active', instance.is_active
        )
        instance.save()

        questions_data = validated_data.get('questions')
        question_list = list(instance.questions.all())
        for question in questions_data:
            try:
                this_question = question_list.pop(0)
                this_question.text = question.get('text', this_question.text)
                this_question.order = question.get('order', this_question.order)
                answers_list = list(this_question.answers.all())
                for answer in question.get('answers'):
                    try:
                        this_answer = answers_list.pop(0)
                        this_answer.text = answer.get('text', this_answer.text)
                        this_answer.is_correct = answer.get('is_correct', this_answer.is_correct)
                        this_answer.save()
                    except IndexError:
                        self.create_answers(answer)
                this_question.save()
            except IndexError:
                self.create_question(question)

        return instance
