from flask import Flask, request, jsonify

app = Flask(__name__)

# data (in-memory-database)
contacts = [
            {'id': 1, 'name': 'usha', 'ph_no': 1234567890},
            {'id': 2, 'name': 'tulasi', 'ph_no': 2345678901},
            {'id': 3, 'name': 'raj', 'ph_no': 3456789012},
            {'id': 4, 'name': 'komal', 'ph_no': 4567890123},
            ]


@app.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify(contacts), 200


@app.route('/contact-list', methods=['GET'])
def get_contacts_list():
    return jsonify(contacts), 201


@app.route('/insert-contact', methods=['POST'])
def insert_contact():
    data = request.get_json()
    new_contact = {
        'id': len(contacts) + 1,
        'name': data.get('name'),
        'ph_no': data.get('ph_no')
    }
    contacts.append(new_contact)
    return jsonify(new_contact), 201


@app.route('/contacts/<int:contact_id>', methods=['PUT'])
def update_contact(contact_id):
    data = request.get_json()
    for item in contacts:
        if item['id'] == contact_id:
            item['name'] = data.get('name')
            item['ph_no'] = data.get('ph_no')
            return jsonify(item)
        return jsonify({'message': 'contact not found'}), 404


@app.route('/contacts/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    for index, item in enumerate(contacts):
        if item['id'] == contact_id:
            del contacts[index]
            return jsonify({'status': 'success', 'id': contact_id,
                            'msg': f'{contact_id} contact has been deleted'})


if __name__ == '__main__':
    app.run(debug=True)
