class Database {
    private client: any;
  
    get connectedClient() {
      if (!this.client) {
        throw new Error('Database not connected!');
      }
      return this.client;
    }
  
    connect() {
      // Establishing connection ...
      this.client = {};
    }
  }