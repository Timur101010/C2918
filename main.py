api_key = 'AIzpSyAq3L9DiPK0KxrGBbdY7wNN7kfPbm_hsPg'  # Введите свой ключ API вместо этого

youtube_api = build('youtube', 'v3', developerKey=api_key)

results = youtube_api.search().list(q=search_terms, part='snippet', type='video',
                                    order='viewCount', maxResults=50).execute()
publishedAt = results['items'][0]['snippet']['publishedAt']


# Функция для подсчета количества просмотров по отношению к подписчикам
def view_to_sub_ratio(viewcount, num_subscribers):
    if num_subscribers == 0:
        return 0
    else:
        ratio = viewcount / num_subscribers
        return ratio

    # Убираем крайние случаи (низкое количество просмотров или подписчиков


def custom_score(viewcount, ratio, days_since_published):
    ratio = min(ratio, 5)
    score = (viewcount * ratio)
    return score


def get_start_date_string(search_period_days):
    """Returns string for date at start of search period."""
    search_start_date = datetime.today() - timedelta(search_period_days)
    date_string = datetime(year=search_start_date.year, month=search_start_date.month,
                           day=search_start_date.day).strftime('%Y-%m-%dT%H:%M:%SZ')
    return date_string


date_string = vf.get_start_date_string(7)
results = youtube_api.search().list(q=search_terms, part='snippet',
                                    type='video', order='viewCount', maxResults=50,
                                    publishedAfter=date_string).execute()


def custom_score(viewcount, ratio, days_since_published):
    ratio = min(ratio, 5)
    score = (viewcount * ratio) / days_since_published
    return score

