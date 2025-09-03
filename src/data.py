events = [
    {
        'id': 1,
        'title': 'Feria de tecnología',
        'slug': 'feria-tecnologia',
        'description': 'Descripción del evento...',
        'date': '2026-03-21',
        'time': '14:00',
        'location': 'Auditorio Principal',
        'category': 'Tecnología',
        'max_attendees': 50,
        'attendees': [{'name': 'Juan Pérez', 'email': 'juan@example.com'}],
        'featured': True
    },
    {
        'id': 2,
        'title': 'Conferencia de Python',
        'slug': 'conferencia-python',
        'description': 'Aprende sobre Python y sus aplicaciones.',
        'date': '2025-09-15',
        'time': '14:00',
        'location': 'Auditorio Principal',
        'category': 'Tecnología',
        'max_attendees': 100,
        'attendees': [],
        'featured': True
    },
    {
        'id': 3,
        'title': 'Taller de Inteligencia Artificial',
        'slug': 'taller-ia',
        'description': 'Explora el mundo de la IA con expertos.',
        'date': '2025-10-10',
        'time': '10:00',
        'location': 'Sala de Conferencias',
        'category': 'Académico',
        'max_attendees': 30,
        'attendees': [],
        'featured': False
    },
    {
        'id': 4,
        'title': 'Festival Cultural',
        'slug': 'festival-cultural',
        'description': 'Disfruta de música, arte y gastronomía.',
        'date': '2025-11-05',
        'time': '18:00',
        'location': 'Plaza Central',
        'category': 'Cultural',
        'max_attendees': 500,
        'attendees': [],
        'featured': True
    },
    {
        'id': 5,
        'title': 'Carrera 5K',
        'slug': 'carrera-5k',
        'description': 'Participa en la carrera anual de 5 kilómetros.',
        'date': '2025-12-01',
        'time': '07:00',
        'location': 'Parque Principal',
        'category': 'Deportivo',
        'max_attendees': 200,
        'attendees': [],
        'featured': False
    },
    {
        'id': 6,
        'title': 'Concierto de Rock',
        'slug': 'concierto-rock',
        'description': 'Vive la experiencia del mejor rock en vivo.',
        'date': '2025-12-15',
        'time': '20:00',
        'location': 'Estadio Municipal',
        'category': 'Cultural',
        'max_attendees': 1000,
        'attendees': [],
        'featured': True
    },
    {
        'id': 7,
        'title': 'Seminario de Marketing Digital',
        'slug': 'seminario-marketing',
        'description': 'Aprende estrategias de marketing digital.',
        'date': '2026-01-20',
        'time': '09:00',
        'location': 'Auditorio Empresarial',
        'category': 'Académico',
        'max_attendees': 50,
        'attendees': [],
        'featured': False
    },
    {
        'id': 8,
        'title': 'Torneo de Ajedrez',
        'slug': 'torneo-ajedrez',
        'description': 'Compite con los mejores jugadores de ajedrez.',
        'date': '2026-02-10',
        'time': '10:00',
        'location': 'Centro Deportivo',
        'category': 'Deportivo',
        'max_attendees': 20,
        'attendees': [],
        'featured': False
    },
    {
        'id': 9,
        'title': 'Exposición de Arte Moderno',
        'slug': 'exposicion-arte',
        'description': 'Admira las obras de artistas contemporáneos.',
        'date': '2026-03-05',
        'time': '16:00',
        'location': 'Galería de Arte',
        'category': 'Cultural',
        'max_attendees': 100,
        'attendees': [],
        'featured': True
    },
    {
        'id': 10,
        'title': 'Hackathon de Desarrollo Web',
        'slug': 'hackathon-web',
        'description': 'Desarrolla soluciones innovadoras en equipo.',
        'date': '2026-04-01',
        'time': '08:00',
        'location': 'Centro Tecnológico',
        'category': 'Tecnología',
        'max_attendees': 150,
        'attendees': [],
        'featured': True
    },
    {
        'id': 11,
        'title': 'Foro de Emprendimiento',
        'slug': 'foro-emprendimiento',
        'description': 'Conoce las claves para emprender con éxito.',
        'date': '2026-05-10',
        'time': '10:00',
        'location': 'Auditorio Empresarial',
        'category': 'Social',
        'max_attendees': 80,
        'attendees': [],
        'featured': False
    }
]


categories = ['Tecnología', 'Académico', 'Cultural', 'Deportivo', 'Social']


def find_event(slug):
    return next((event for event in events if event['slug'] == slug), None)

def get_next_id():
    return len(events) + 1

def is_event_full(event):
    return len(event['attendees']) >= event['max_attendees']
