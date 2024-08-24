from django.db import models

class Wish(models.Model):
    # 소원 제목 및 내용
    title = models.CharField(max_length=100)
    content = models.TextField()

    # 카테고리 선택지
    CATEGORY_CHOICES = [
        ('career', '진로'),
        ('health', '건강'),
        ('relationship', '인간 관계'),
        ('money', '돈'),
        ('goal', '목표'),
        ('study', '학업/성적'),
        ('etc', '기타'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    # 생성 시간
    created_at = models.DateTimeField(auto_now_add=True)

    # 승인 상태 선택지
    PENDING = 'pending'
    APPROVED = 'approved'
    REJECTED = 'rejected'
    CONFIRM_STATUS_CHOICES = [
        (PENDING, '보류됨'),
        (APPROVED, '승인됨'),
        (REJECTED, '거절됨'),
    ]
    is_confirm = models.CharField(max_length=10, choices=CONFIRM_STATUS_CHOICES, default=PENDING)

    # 소프트 삭제를 위한 필드
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title