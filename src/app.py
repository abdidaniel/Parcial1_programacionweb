from flask import Flask, render_template, redirect, url_for, flash
from forms import EventForm, RegistrationForm
from data import events, categories, find_event, get_next_id, is_event_full

app = Flask(__name__)
app.secret_key = 'mysecretkey'


@app.route('/')
def index():
    upcoming = [event for event in events if event['date'] >= '2025-09-01']
    featured_events = [event for event in events if event.get('featured', False)]
    return render_template('index.html', events=upcoming, featured_events=featured_events)

@app.route('/event/<slug>/')
def event_detail(slug):
    event = find_event(slug)
    if event is None:
        return 'Evento no encontrado', 404
    return render_template('event_detail.html', event=event)


@app.route('/admin/event/', methods=['GET', 'POST'])
def create_event():
    form = EventForm()
    if form.validate_on_submit():
        new_event = {
            'id': get_next_id(),
            'title': form.title.data,
            'slug': form.title.data.lower().replace(' ', '-'),
            'description': form.description.data,
            'date': form.date.data.strftime('%Y-%m-%d'),
            'time': form.time.data.strftime('%H:%M'),
            'location': form.location.data,
            'category': form.category.data,
            'max_attendees': form.max_attendees.data,
            'attendees': [],
            'featured': form.featured.data
        }
        events.append(new_event)  # Modificar la lista global de eventos
        flash('Evento creado exitosamente', 'success')
        return redirect(url_for('index'))
    return render_template('create_event.html', form=form)

@app.route('/event/<slug>/register/', methods=['GET', 'POST'])
def register(slug):
    event = find_event(slug)
    if event is None or is_event_full(event):
        flash('No se puede registrar, el evento está lleno o no existe.', 'danger')
        return redirect(url_for('event_detail', slug=slug))

    form = RegistrationForm()
    if form.validate_on_submit():
        # Validar duplicados
        if any(attendee['email'] == form.email.data for attendee in event['attendees']):
            flash('Ya estás registrado en este evento.', 'warning')
        else:
            event['attendees'].append({'name': form.name.data, 'email': form.email.data})
            flash('Te has registrado exitosamente al evento', 'success')
        return redirect(url_for('event_detail', slug=slug))

    return render_template('register.html', form=form, event=event)

@app.route('/events/category/<category>/')
def events_by_category(category):
    filtered_events = [event for event in events if event['category'].lower() == category.lower()]
    if not filtered_events:
        flash(f'No hay eventos en la categoría "{category}".', 'info')
    return render_template('category.html', events=filtered_events, category=category)


if __name__ == '__main__':
    app.run(debug=True)

