const {Datastore} = require('@google-cloud/datastore');
const express = require('express');
const app = express();
const datastore = new Datastore();

app.use(express.json());

// Part I: Base page
app.get('/', (req, res) => {
  res.send('Hello World!');
});

// Part II: /register using Datastore mode
app.post('/register', async (req, res) => {
  const username = req.body.username;
  const userKey = datastore.key(['User', username]);
  await datastore.save({
    key: userKey,
    data: { username: username },
  });
  res.status(200).json({ message: 'User registered' });
});

// Part II: /list returning { users: [...] }
app.get('/list', async (req, res) => {
  const query = datastore.createQuery('User');
  const [users] = await datastore.runQuery(query);
  const usernames = users.map((user) => user.username);
  res.json({ users: usernames });
});

// Part II: /clear MUST be a POST request
app.post('/clear', async (req, res) => {
  const query = datastore.createQuery('User');
  const [users] = await datastore.runQuery(query);
  const keys = users.map((user) => user[datastore.KEY]);
  if (keys.length > 0) {
    await datastore.delete(keys);
  }
  res.status(200).json({ message: 'Cleared' });
});

// Part I Requirement: Port 8080
app.listen(8080, '0.0.0.0', () => {
  console.log('Server running on port 8080');
});
