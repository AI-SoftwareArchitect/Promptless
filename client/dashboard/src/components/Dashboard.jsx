import React, { useState } from "react";
import { useQuery, gql } from "@apollo/client";
import {
  Grid,
  Card,
  CardContent,
  Typography,
  Button,
  Collapse,
  AppBar,
  Toolbar,
  Container,
  Box,
} from "@mui/material";
import { red, blue, purple } from "@mui/material/colors";

const GET_FILES = gql`
  query GetFiles {
    files {
      filename
      content
    }
  }
`;

const colors = {
  "errors.txt": red[500],
  "commands.txt": blue[500],
  "memory.txt": purple[500],
};

export default function Dashboard() {
  const { loading, error, data } = useQuery(GET_FILES, {
    pollInterval: 3000,
  });

  const [expandedFile, setExpandedFile] = useState(null);

  if (loading) return <p>Yükleniyor...</p>;
  if (error) return <p>Hata: {error.message}</p>;

  const getLastEntries = (content) => {
    return content
      .split("\n")
      .filter((line) => line.trim() !== "")
      .slice(-10)
      .reverse();
  };

  return (
    <Box>
      <AppBar position="static" sx={{ mb: 4 }}>
        <Toolbar>
          <Typography variant="h5" component="div" sx={{ flexGrow: 1 }}>
            Promptless Dashboard
          </Typography>
        </Toolbar>
      </AppBar>

      <Container>
        <Grid container spacing={4}>
          {data.files.map(({ filename, content }) => {
            const entries = getLastEntries(content);
            const lastEntry = entries[0] || "Veri bulunamadı.";
            const color = colors[filename] || "#ccc";
            const label = filename.replace(".txt", "").toUpperCase();

            return (
              <Grid item xs={12} sm={6} md={4} key={filename}>
                <Card>
                  <CardContent>
                    <Typography variant="h6" gutterBottom>
                      {label}
                    </Typography>
                    <Typography
                      variant="body2"
                      style={{
                        whiteSpace: "pre-wrap",
                        wordBreak: "break-word",
                        marginBottom: "1rem",
                      }}
                    >
                      {lastEntry}
                    </Typography>
                    <Button
                      variant="contained"
                      onClick={() =>
                        setExpandedFile(
                          expandedFile === filename ? null : filename
                        )
                      }
                      sx={{ backgroundColor: color }}
                    >
                      Son 10 Kaydı Görüntüle
                    </Button>
                    <Collapse in={expandedFile === filename} timeout="auto" unmountOnExit>
                      <Box mt={2}>
                        {entries.map((entry, index) => (
                          <Card key={index} sx={{ maxHeight: 100 , mb: 1, p: 1, color: "black", backgroundColor: "#f5f5f5" }}>
                            <Typography variant="body2">{entry}</Typography>
                          </Card>
                        ))}
                      </Box>
                    </Collapse>
                  </CardContent>
                </Card>
              </Grid>
            );
          })}
        </Grid>
      </Container>
    </Box>
  );
}