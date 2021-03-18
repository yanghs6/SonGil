import { render, screen } from '@testing-library/react';
import App from './view/App';
import App2 from './view/App2';

test('renders learn react link', () => {
  // render(<App />);
  // render(<App2 />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
