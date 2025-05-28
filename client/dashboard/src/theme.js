import { createTheme } from '@mui/material/styles';

const theme = createTheme({
  palette: {
    mode: 'dark',
    background: { default: '#000', paper: '#111' },
    text: { primary: '#fff', secondary: '#aaa' },
  },
  components: {
    MuiCard: {
      styleOverrides: {
        root: { borderRadius: 16, minHeight: 200 },
      },
    },
  },
});

export default theme;
